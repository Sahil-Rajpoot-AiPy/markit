import pytest
from PIL import Image
import os
import config
import files_utils as fu
import img_utils as iu


def test_resource_path():
    p = config.resource_path("data/markit_icon.ico")
    assert os.path.isabs(p)


def test_png_selector(monkeypatch):
    monkeypatch.setattr(fu.filedialog, "askopenfilename", lambda **k: "fake/logo.png")
    fu.png_file = ""
    fu.png_selector()
    assert fu.png_file == "fake/logo.png"


def test_final_folder(monkeypatch):
    monkeypatch.setattr(fu.filedialog, "askdirectory", lambda **k: "fake/out")
    fu.output_folder = ""
    fu.final_folder()
    assert fu.output_folder == "fake/out"


def test_img_list(monkeypatch):
    monkeypatch.setattr(fu.filedialog, "askdirectory", lambda **k: "fake/in")
    monkeypatch.setattr(fu.os, "listdir", lambda folder: ["a.png", "b.txt"])
    monkeypatch.setattr(fu.config, "ALLOWED_EXTENSIONS", (".png", ".jpg"))
    fu.input_imgs_list = []
    fu.img_list()
    expected = [os.path.join("fake/in", "a.png")]
    assert fu.input_imgs_list == expected


def test_open_wm_png(monkeypatch):
    fu.png_file = "fake/logo.png"
    monkeypatch.setattr(iu.Image, "open", lambda f: Image.new("RGBA", (10, 10)))
    im = iu.open_wm_png()
    assert isinstance(im, Image.Image)


def test_auto_logo_resizing():
    img = Image.new("RGBA", (200, 100))
    logo = Image.new("RGBA", (50, 25))
    r = iu.auto_logo_resizing(logo, img)
    assert isinstance(r, Image.Image)
    assert r.width != logo.width


def test_auto_logo_placement(monkeypatch):
    img = Image.new("RGBA", (100, 50))
    logo = Image.new("RGBA", (20, 10))
    for p in iu.placement_opts:
        iu.placement = p
        x, y = iu.auto_logo_placement(logo, img)
        assert 0 <= x <= img.width - logo.width
        assert 0 <= y <= img.height - logo.height
    iu.placement = "bad"
    with pytest.raises(ValueError):
        iu.auto_logo_placement(logo, img)


def test_auto_logo_transparency():
    logo = Image.new("RGBA", (30, 15), (255, 0, 0, 255))
    iu.opacity = 50
    iu.auto_logo_transparency(logo)  # modifies in place
    min_alpha, max_alpha = logo.split()[3].getextrema()
    assert max_alpha <= 255
    assert min_alpha >= 0


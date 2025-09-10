def create_button(self, row, column, text, command, height=None, width=None, font=None):
    kwargs = {"text": text, "command": command}
    if font is not None:
        kwargs["font"] = font
    if height is not None:
        kwargs["height"] = height
    if width is not None:
        kwargs["width"] = width

    button = ctk.CTkButton(self, **kwargs)
    button.grid(row=row, column=column, padx=10, pady=10)
    return button

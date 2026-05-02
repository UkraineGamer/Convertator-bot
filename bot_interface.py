class Bot_interface:
    def __init__(self):
        self.conversion_type = ""
        self.output = ""
        self.language_chosen = ""

    def first_choice(self, for_inline_keyboard_button, for_inline_keyboard_markup):
        keyboard = for_inline_keyboard_markup([
            [
                for_inline_keyboard_button("Video", callback_data="type:video"),
                for_inline_keyboard_button("Audio", callback_data="type:audio"),
                for_inline_keyboard_button("Image", callback_data="type:image"),
            ]
        ])
        return keyboard

    def if_video(self, for_inline_keyboard_button, for_inline_keyboard_markup):
        keyboard = for_inline_keyboard_markup([
            [
                for_inline_keyboard_button(".MP4", callback_data="ext:.mp4"),
                for_inline_keyboard_button(".MOV", callback_data="ext:.mov"),
                for_inline_keyboard_button(".MKV", callback_data="ext:.mkv"),
            ]
        ])
        return keyboard

    def if_audio(self, for_inline_keyboard_button, for_inline_keyboard_markup):
        keyboard = for_inline_keyboard_markup([
            [
                for_inline_keyboard_button(".MP3", callback_data="ext:.mp3"),
                for_inline_keyboard_button(".AAC", callback_data="ext:.aac"),
                for_inline_keyboard_button(".OGG", callback_data="ext:.ogg"),
            ]
        ])
        return keyboard

    def if_image(self, for_inline_keyboard_button, for_inline_keyboard_markup):
        keyboard = for_inline_keyboard_markup([
            [
                for_inline_keyboard_button(".JPG", callback_data="ext:.jpg"),
                for_inline_keyboard_button(".JPEG", callback_data="ext:.jpeg"),
                for_inline_keyboard_button(".PNG", callback_data="ext:.png"),
            ]
        ])
        return keyboard

    def extension_choice(self, conversion_type, for_inline_keyboard_button, for_inline_keyboard_markup):
        self.conversion_type = conversion_type
        if conversion_type == "video":
            return self.if_video(for_inline_keyboard_button, for_inline_keyboard_markup)
        if conversion_type == "audio":
            return self.if_audio(for_inline_keyboard_button, for_inline_keyboard_markup)
        return self.if_image(for_inline_keyboard_button, for_inline_keyboard_markup)

    def set_extension(self, extension):
        self.output = extension

    def output_clear(self):
        self.output = ""
        self.conversion_type = ""

    def language_clear(self):
        self.language_chosen = ""

    def language_choice(self, for_inline_keyboard_button, for_inline_keyboard_markup):
        keyboard = for_inline_keyboard_markup([
            [
            for_inline_keyboard_button("ENG", callback_data = "lang:ENG"),
            for_inline_keyboard_button("UA", callback_data = "lang:UA"),
            ]
        ])
        return keyboard
    
    def language_in_use(self, language):
        self.language_chosen = language
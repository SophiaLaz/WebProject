from hashlib import sha256


class Actor:
    def __init__(self, name: str, info: str, image: str, link: str):
        self.name = name
        self.info = info
        self.image = image
        self.link = link

    def _get_color(self) -> str:
        hash_code = sha256(self.name.encode()).hexdigest()
        code = int(hash_code[:8], 16)
        r, g, b = code % 256, code // 256 % 256, code // 256 // 256 % 256
        return f'rgb({r}, {g}, {b})'

    def create_dict(self) -> dict:
        return {'name': self.name, 'info': self.info, 'image': self.image, 'link': self.link,
                'color': self._get_color()}

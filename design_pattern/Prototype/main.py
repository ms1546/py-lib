import copy

class DocumentPrototype:
    """プロトタイプの抽象クラス。クローンを作成するメソッドを定義。"""
    def clone(self):
        pass

class Document(DocumentPrototype):
    """具体的なドキュメントクラス。プロトタイプを実装し、自己のディープコピーを作成。"""
    def __init__(self, text, images):
        self.text = text
        self.images = images

    def clone(self):
        """ディープコピーを使用してドキュメントの完全な複製を作成する。"""
        return copy.deepcopy(self)

    def __str__(self):
        return f"Document(text={self.text}, images={self.images})"

original_document = Document("Hello, World!", ["image1.jpg", "image2.jpg"])
print("Original:", original_document)

cloned_document = original_document.clone()
print("Cloned:", cloned_document)

cloned_document.text = "This is a cloned document."
cloned_document.images.append("image3.jpg")
print("Modified Original:", original_document)
print("Modified Cloned:", cloned_document)

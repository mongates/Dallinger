from .models import Meme


class Genome(Meme):
    __mapper_args__ = {"polymorphic_identity": "genome"}


class Mimeme(Meme):
    __mapper_args__ = {"polymorphic_identity": "mimeme"}

from mongoengine import *


class FeatureModel(EmbeddedDocument):

    feature_class = IntField()
    feature_value = FloatField()
    feature_type = StringField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.feature_type, self.feature_value, self.feature_class)


class StudyModel(Document):

    name = StringField(max_length=250)
    features = EmbeddedDocumentListField(document_type=FeatureModel)

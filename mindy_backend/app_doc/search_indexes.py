from haystack import indexes
from app_doc.models import *

# 文档索引
class DocIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    top_doc = indexes.IntegerField(model_attr='top_doc')
    modify_time = indexes.DateTimeField(model_attr='modify_time')

    def get_model(self):
        return Doc

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status=1)
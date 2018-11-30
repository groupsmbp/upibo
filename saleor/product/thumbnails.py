from celery import shared_task

from ..core.utils import create_thumbnails
from .models import ProductImage, ImageData


@shared_task
def create_product_thumbnails(image_id):
    """Takes ProductImage model, and creates thumbnails for it."""
    create_thumbnails(pk=image_id, model=ProductImage, size_set='products')

@shared_task
def create_gallery_thumbnails(image_id):
    """Takes ProductImage model, and creates thumbnails for it."""
    create_thumbnails(pk=image_id, model=ImageData, size_set='products')

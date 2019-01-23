from rest_framework.routers import SimpleRouter

from .views import CategoryView, ProductView

router = SimpleRouter()
router.register(r'products', ProductView)
router.register(r'categories', CategoryView)

urlpatterns = [
]

urlpatterns += router.urls

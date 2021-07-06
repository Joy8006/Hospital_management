from .views import HospitalViewSet, PatientViewSet, ReportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("patients", PatientViewSet)
router.register("reports", ReportViewSet)
router.register("hospitals", HospitalViewSet)

urlpatterns = router.urls

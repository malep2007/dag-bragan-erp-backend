from rest_framework import serializers, mixins, generics
from customer.models import Inquiry, Customer

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = (
            'id',
            'recorded_by',
            'inspection_date',
            'extra_details',
            'date_created',
            'inq_number',
            'approve_job'
        )

    approve_job = serializers.BooleanField(default=False)


class InquiryDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'business_name', 'location', 'first_name',
                  'last_name', 'middle_name', 'phone_number', 'inquiry')


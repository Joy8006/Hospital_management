from rest_framework import serializers
from django.utils import timezone


class DateRangeSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()

    def validate(self, data):
        offset = self.context["request"].tzoffset

        today = timezone.now().date() - timezone.timedelta(minutes=offset)
        start = data['start']
        end = data['end']

        if start > end:
            message = 'End date should not greater than start date.'
            raise serializers.ValidationError({"message": message})

        if start > today or end > today:
            message = 'Date should not greater than today.'
            raise serializers.ValidationError({"message": message})

        return data
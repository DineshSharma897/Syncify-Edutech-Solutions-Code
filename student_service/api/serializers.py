from rest_framework import serializers
from .models import Student, Test

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'department']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'student', 'subject', 'score', 'max_score', 'date']

        def validate(self, data):
            score = data.get('score')
            max_score = data.get('max_score')
            if max_score is not None and max_score <=0:
                raise serializers.ValidationError("max_score must be  > 0")
            if score is not None and max_score is not None and score > max_score:
                raise serializers.ValidationError("Score cannot exceed max_score")
            if score is not None and score < 0:
                raise serializers.ValidationError("Score cannot be negative")
            return data
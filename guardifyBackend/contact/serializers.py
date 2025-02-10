from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def validate_email(self, value):
        """Check if email is valid."""
        if '@' not in value:
            raise serializers.ValidationError("Email is not valid")
        return value

    def validate(self, attrs):
        """Validate all the data."""
        # Check if name is not empty
        if not attrs.get('name'):
            raise serializers.ValidationError({"name": "Name cannot be empty."})

        # Check if subject is not empty
        if not attrs.get('subject'):
            raise serializers.ValidationError({"subject": "Subject cannot be empty."})

        # Check if message is not empty
        if not attrs.get('message'):
            raise serializers.ValidationError({"message": "Message cannot be empty."})

        return attrs
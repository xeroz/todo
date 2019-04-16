from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user_data'] = {
            'user_name': self.user.username,
            'name': self.user.first_name,
            'last_name': self.user.last_name,
        }

        return data



# Create your views here.
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductTableSerializer, UserTableSerializer
from .models import ProductTable, UserTable

class SignupView(APIView):
    def post(self, request):
        serializer = UserTableSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            
           
            # Additional validation checks can be added here

            serializer.save()
            return Response({'message': 'Account created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(request.data)
        try:
            obj = UserTable.objects.filter(email=email,password=password)

           
            if obj:

                # request.session['role'] = 'user'
                # request.session['email'] = sanitized_email
                # request.session['isloggedin'] = True
                return Response({'message': 'Logged In'})
            else:
                
                return Response({'message': "user not found"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print('Error executing SQL query:', e)
            return Response({'message': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

class ProductDetailsView(APIView):
    def get(self, request):
        image_url = request.query_params.get('image_url')

        if image_url:
            try:
                connection = pool.getConnection()
                cursor = connection.cursor()

                sql = "SELECT * FROM gotera_product_table WHERE product_image_url = %s"
                cursor.execute(sql, (image_url,))
                result = cursor.fetchall()

                if len(result) == 0:
                    return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(result)

            except Exception as e:
                print('Error executing SQL query:', e)
                return Response({'message': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            finally:
                cursor.close()
                connection.close()

        else:
            return Response({'message': 'Image URL parameter is missing.'}, status=status.HTTP_400_BAD_REQUEST)
        


class ProductListView(APIView):
    def get(self, request):
        queryset = ProductTable.objects.all()
        serializer = ProductTableSerializer(queryset, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)



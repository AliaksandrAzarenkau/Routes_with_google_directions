from django.http import HttpResponseRedirect
from rest_framework import status, generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages

from route.serializers import CartAddProductSerializer
from client.models import Client, ClientObjectsProfile
from client.serializers import ClientCreateSerializer, ClientObjectsProfileSerializer, ClientListSerializer


class ClientAPIVew(generics.ListAPIView):
    queryset = Client.objects.all()
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'client_create.html'
    serializer_class = ClientCreateSerializer

    def get(self, request, *args, **kwargs):
        """Получение данных клиентов"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'clients': queryset, 'serializer': serializer}
            return Response(context, template_name=self.template_name)
        else:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Добавление данных клиента"""

        if not request.data['organisation_name']:
            context = messages.error(request, 'Введите наименование организации')
            return HttpResponseRedirect('./client_create', content=context)

        if not request.data['phone']:
            context = messages.error(request, 'Введите номер телефона')
            return HttpResponseRedirect('./client_create', content=context)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if request.accepted_renderer.format == 'html':
            message = "Клиент добавлен"
            messages.success(request, message)
            return redirect('./client_create')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientProfileAPIVew(generics.ListAPIView):
    queryset = ClientObjectsProfile.objects.all()
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'client_profile.html'
    serializer_class = ClientObjectsProfileSerializer

    def get(self, request, *args, **kwargs):
        """Получение данных объекта клиентов"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'clients': queryset, 'serializer': serializer}
            return Response(context, template_name=self.template_name)
        else:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Добавление данных объекта клиента"""
        serializer = self.serializer_class.create(request, request.data)

        if request.accepted_renderer.format == 'html':
            message = "Объект добавлен"
            messages.success(request, message)
            return redirect('./client_profile')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'client_list.html'

    def get(self, request, *args, **kwargs):
        """Получаем список всех клиентов"""
        clients = self.serializer_class.get_clients(request)
        context = {'clients': clients}

        return Response(context, template_name=self.template_name)


class ClientObjectsListAPIView(generics.ListAPIView):
    serializer_class = ClientListSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'client_objects_list.html'

    def get(self, request, pk):
        data = self.serializer_class.get_objects(request, pk=pk)
        context = {'client_name': data['client_name'], 'client_obj': data['client_obj']}

        return Response(context, template_name=self.template_name)


def product_detail(request, pk):
    product = get_object_or_404(
        ClientObjectsProfile,
        id=pk,
        available=True
    )
    serializer = CartAddProductSerializer()
    return (render
            (request,
             'detail.html',
             {
                 'product': product,
                 'cart_product_form': serializer})
            )



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'  # Use 'id' as the lookup field for retrieving a specific event
    
    def add_file_to_event(request, event_id):
        event = Event.objects.get(id=event_id)
        files = {"image": "event_image.jpg"}
        event.set_files(files)
        event.save()

    def get_queryset(self):
        return Event.objects.filter(id=1)  # Get only the event with id=1

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Creating a new event is not allowed."}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Deleting the event is not allowed."}, status=status.HTTP_403_FORBIDDEN)

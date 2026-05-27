from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .services import (
    process_sap_file,
    process_utility_file,
    process_travel_file
)

from .models import *
from .serializers import *

from .services import process_sap_file


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_sap(request):

    if request.method == 'POST':

        file = request.FILES.get('file')

        if not file:
            return Response({
                "error": "No file uploaded"
            })

        process_sap_file(file)

        return Response({
            "message": "SAP File Uploaded Successfully"
        })

    return Response({
        "message": "Use POST method to upload CSV file"
    })


@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all()

    serializer = EmissionRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def approve_record(request, id):

    record = EmissionRecord.objects.get(id=id)

    old_status = record.status

    record.status = 'approved'

    record.save()

    AuditLog.objects.create(
        record=record,
        action='Approved',
        old_value=old_status,
        new_value='approved'
    )

    return Response({
        "message": "Record Approved"
    })

@api_view(['POST'])
def reject_record(request, id):

    record = EmissionRecord.objects.get(id=id)

    old_status = record.status

    record.status = 'rejected'

    record.save()

    AuditLog.objects.create(
        record=record,
        action='Rejected',
        old_value=old_status,
        new_value='rejected'
    )

    return Response({
        "message": "Record Rejected"
    })


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_sap(request):

    if request.method == 'POST':

        uploaded_file = request.FILES.get('file')

        if uploaded_file is None:
            return Response({
                "error": "No file uploaded"
            })

        process_sap_file(uploaded_file)

        return Response({
            "message": "SAP File Uploaded Successfully"
        })

    return Response(status=200)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_utility(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        })

    process_utility_file(file)

    return Response({
        "message": "Utility File Uploaded Successfully"
    })

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_travel(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        })

    process_travel_file(file)

    return Response({
        "message": "Travel File Uploaded Successfully"
    })

def upload_page(request):

    if request.method == 'POST':

        file = request.FILES.get('file')

        source_type = request.POST.get('source_type')

        if file:

            if source_type == 'sap':

                process_sap_file(file)

            elif source_type == 'utility':

                process_utility_file(file)

            elif source_type == 'travel':

                process_travel_file(file)

            return redirect('/dashboard/')

    return render(
        request,
        'myapp/upload.html'
    )


# Dashboard Page
def dashboard_page(request):

    records = EmissionRecord.objects.all()

    return render(
        request,
        'myapp/dashboard.html',
        {'records': records}
    )


# Review Page
def review_page(request):

    records = EmissionRecord.objects.all()

    return render(
        request,
        'myapp/review.html',
        {'records': records}
    )


# Approve Page
def approve_page(request, id):

    record = EmissionRecord.objects.get(id=id)

    old_status = record.status

    record.status = 'approved'

    record.save()

    AuditLog.objects.create(
        record=record,
        action='Approved',
        old_value=old_status,
        new_value='approved'
    )

    return redirect('/review/')


# Reject Page
def reject_page(request, id):

    record = EmissionRecord.objects.get(id=id)

    old_status = record.status

    record.status = 'rejected'

    record.save()

    AuditLog.objects.create(
        record=record,
        action='Rejected',
        old_value=old_status,
        new_value='rejected'
    )

    return redirect('/review/')
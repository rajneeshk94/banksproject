from django.http import JsonResponse
from rest_framework.decorators import api_view
from banksAPI.utils import get_csv_data
import json


@api_view(['GET'])
def bank_list(request):
    data = get_csv_data()
    banks = []
    for row in data:
        bank = {
            "id": row["bank_id"],
            "name": row["bank_name"]
        }
        if bank not in banks:
            banks.append(bank)
    return JsonResponse(banks, safe=False)


@api_view(['GET'])
def branch_list(request, bank_id):
    data = get_csv_data()
    branches = []
    for row in data:
        if row["bank_id"] == bank_id:
            branch = {
                "ifsc": row["ifsc"],
                "branch": row["branch"],
                "address": row["address"],
                "city": row["city"],
                "district": row["district"],
                "state": row["state"]
            }
            branches.append(branch)

    if len(branches) == 0:
        response_data = {'error': f'Bank with bank id {bank_id} not found'}
        return JsonResponse(response_data, status=404)

    return JsonResponse(branches, safe=False)


@api_view(['GET'])
def ifsc_details(request, ifsc_code):
    data = get_csv_data()

    branch = next((b for b in data if b['ifsc'] == ifsc_code), None)

    if branch is None:
        response_data = {'error': f'Branch with IFSC code {ifsc_code} not found'}
        return JsonResponse(response_data, status=404)

    for row in data:
        if row["ifsc"] == ifsc_code:
            branch = {
                "ifsc": row["ifsc"],
                "bank_id": row["bank_id"],
                "branch_name": row["branch"],
                "address": row["address"],
                "city": row["city"],
                "district": row["district"],
                "state": row["state"]
            }
            
    return JsonResponse(branch, safe=False)

    # branch = next((b for b in data if b['ifsc'] == ifsc_code), None)
    # if branch is None:
    #     response_data = {'error': f'Branch with IFSC code {ifsc_code} not found'}
    #     return JsonResponse(response_data, status=404)
    # response_data = json.dumps(branch)
    # return JsonResponse(response_data, safe=False)

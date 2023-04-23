from Lib import Database
from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from .SaveTransaction import save_transaction
from .DeleteTransaction import delete_transaction
from .GetTransaction import get_transaction
from .GetFromHumans import get_from_humans

blueprint = Blueprint('Transaction', __name__)

@blueprint.route("/Transaction/SaveTransaction", methods=['GET'])
@cross_origin()
def SaveTransaction():
    transaction_data = request.args.to_dict()

    # Extract the transaction data from the request
    TransactionId = transaction_data.get('TransactionId', None)
    TransactionDate = transaction_data.get('TransactionDate', None)
    FromHumanId = transaction_data.get('FromHumanId', None)
    ToHumanId = transaction_data.get('ToHumanId', None)
    TransactionType = transaction_data.get('TransactionType', None)
    Notes = transaction_data.get('Notes', None)
    Act = transaction_data.get('Act', None)
    Page = transaction_data.get('Page', None)
    NotaryHumanId = transaction_data.get('NotaryHumanId', None)
    Volume = transaction_data.get('Volume', None)
    URL = transaction_data.get('URL', None)
    UserId = transaction_data.get('UserId', None)

    # Call the save_transaction function from SaveTransaction.py with the extracted data
    result = save_transaction(TransactionId, TransactionDate, FromHumanId, ToHumanId, TransactionType, Notes, Act, Page, NotaryHumanId, Volume, URL, UserId)

    return result
    
    

@blueprint.route("/Transaction/DeleteTransaction", methods=['GET'])
@cross_origin()
def DeleteTransaction():
    # Get the transaction data from the request
    transaction_data = request.args.to_dict()

    # Get the transaction ID from the request
    TransactionId = transaction_data.get('TransactionId')
    # Call the delete_transaction function from DeleteTransaction.py
    result = delete_transaction(TransactionId)
    return result

@blueprint.route("/Transaction/GetTransaction", methods=['GET'])
@cross_origin()
def GetTransaction():
    # Get the transaction data from the request
    transaction_data = request.args.to_dict()

    # Get the transaction ID from the request
    TransactionId = transaction_data.get('TransactionId')
    # Call the get_transaction function from GetTransaction.py
    result = get_transaction(TransactionId)
    return result


@blueprint.route("/Transaction/GetFromHumans", methods=['GET'])
@cross_origin()
def GetFromHumans():
    # Get the transaction data from the request
    transaction_data = request.args.to_dict()

    # Call the get_transaction function from GetTransaction.py
    result = get_from_humans()
    return result
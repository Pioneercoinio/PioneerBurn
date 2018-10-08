import jsonschema
import pytest

import validate_message

@pytest.mark.parametrize('description,message,valid', [
    ('Empty string is not a dictionary',
        '', False),
    ('missing required and unknown property',
     {
        "address": 12345        
    }, False),
    ('valid message',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, True),
    ('missing required parameter', 
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('misspelled property',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_ammount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('pcoin address too long',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173b",
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('pcoin address too short',
    {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k17",
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('pcoin address wrong type',
     {
        "pcoin_address": 123445,
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('pcoin amount wrong type',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": 123445,
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('declaration time wrong format',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": "123445",
        "declaration_time": "2018100822:03:25",
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('declaration time wrong type',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": "123445",
        "declaration_time": 12345,
        "eth_address": "0x1234567890ABCDEFabcdef1234567890ABCDEFab"
    }, False),
    ('eth address wrong format',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": "0x1234567890ABCDEGabcdef1234567890ABCDEFab"
    }, False),
    ('eth address wrong type',
     {
        "pcoin_address": "PLdj5g0Wk010SRK0C2knSW3knf2cf0k173",
        "pcoin_amount": "123445",
        "declaration_time": "20181008-22:03:25",
        "eth_address": 12345
    }, False),
])
def test_validate_fails(description, message, valid):
    if valid:
        assert validate_message.validate_message_text(message) is True
    else:
        with pytest.raises(jsonschema.exceptions.ValidationError):
            validate_message.validate_message_text(message)

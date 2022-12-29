from marshmallow import Schema, fields, validate

# These are the projects that will be consuming the API
program = ["adtraction", "tradedoubler", "awin", "adrecord", "misc"]


class CommissionSchema(Schema):
    value = fields.Str(required=True)
    program = fields.Str(required=True, validate=validate.OneOf(program))


class CommissionPayloadSchema(Schema):
    results = CommissionSchema()
    date = fields.Str(required=True)

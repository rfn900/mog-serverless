from marshmallow import Schema, fields, validate

# These are the projects that will be consuming the API
origin = ["fitnessfia", "superstorken", "fiasmode", "marsianog", "marseo"]


class ContactFormSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    origin = fields.Str(required=True, validate=validate.OneOf(origin))
    website = fields.Str()
    message = fields.Str()
    phone = fields.Str()

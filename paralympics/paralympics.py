from flask import current_app as app


@app.route('/')
def hello():
    return f"Hello!"

from paralympics.schemas import RegionSchema, EventSchema

# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()
events_schema = EventSchema(many=True)
event_schema = EventSchema()

from paralympics import db
from paralympics.models import Region

@app.get("/regions")
def get_regions():
    """Returns a list of NOC regions and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result


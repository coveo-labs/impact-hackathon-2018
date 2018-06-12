import json
values = dict()
type = ''
# Get all Crawler values
for m in document.get_meta_data():
    type=':'+m.origin
    for metadata_name, metadata_value in m.values.iteritems():
        values[metadata_name+type] = metadata_value

# Add the allmetadatavalues metadata
document.add_meta_data({"allmetadatavalues": json.dumps(values)})

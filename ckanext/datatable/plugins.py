import ckan as ckan
import ckan.plugins as p
import ckan.lib.helpers as h
import ckan.model as model
import json
import webhelpers.html as html

class WetDataTables(p.SingletonPlugin):
    """
    Plugin for the WET Datatable Resource Previewer. This extension depends upon the CKANEXT-WET-BOEW extension.
    """      
    p.implements(p.IConfigurer)
    p.implements(p.IResourcePreview, inherit=True)

    def update_config(self, config):
        ''' Set up the resource library, public directory and
        template directory for the preview
        '''
        p.toolkit.add_template_directory(config, 'templates/datatable')

    def can_preview(self, data_dict):
        # if the resource is in the datastore then we can preview it with the datatable
        if data_dict['resource'].get('datastore_active'):
            return True
        else:
            return False

    def preview_template(self, context, data_dict):
        return 'wet_datatable.html'

    def setup_template_variables(self, context, data_dict):
        #import pdb;pdb.set_trace()
        dsq_results = ckan.logic.get_action('datastore_search')(context, {'resource_id': data_dict['resource']['id']})
        p.toolkit.c.dsfields = dsq_results['fields']
        p.toolkit.c.dsrecords = dsq_results['records']
        
#  May need to monkey patch CKAN to get rid of iframe #}



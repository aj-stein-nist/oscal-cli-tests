ALL_TESTS = [
    {
        'description': 'main help menu without args',
        'command_args': [],
        'returncode_match': 3,
        'stdout_match': 'usage: oscal-cli <command>',
        'stderr_match': None,
        'exception_match': None        
    },
    {
        'description': 'version command',
        'command_args': ['--version'],
        'returncode_match': 0,
        'stdout_match': 'oscal-cli version 0.0.2-SNAPSHOT built on 2022-06-29 15:23 on commit 41a9ca8\r\nOSCAL version v1.0.4 on commit d3a2b99',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'validate SSP json',
        'command_args': [
            'ssp',
            'validate',
            '--as=json',
            './fedramp-content/dist/content/templates/ssp/json/FedRAMP-SSP-OSCAL-Template.json'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s)',
        'stderr_match': 'ERROR',
        'exception_match': None
    },
    {
        'description': 'validate SSP xml',
        'command_args': [
            'ssp',
            'validate',
            '--as=xml',
            './fedramp-content/dist/content/templates/ssp/xml/FedRAMP-SSP-OSCAL-Template.xml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s)',
        'stderr_match': 'ERROR',
        'exception_match': None
    },
    {
        'description': 'validate SSP yaml',
        'command_args': [
            'ssp',
            'validate',
            '--as=yaml',
            './fedramp-content/dist/content/templates/ssp/yaml/FedRAMP-SSP-OSCAL-Template.yaml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has schema validation',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'validate catalog json',
        'command_args': [
            'catalog',
            'validate',
            '--as=json',
            './oscal-content/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s).',
        'stderr_match': 'depends-on is deprecated',
        'exception_match': None
    },
    {
        'description': 'validate catalog xml',
        'command_args': [
            'catalog',
            'validate',
            '--as=xml',
            './oscal-content/nist.gov/SP800-53/rev5/xml/NIST_SP-800-53_rev5_catalog.xml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s).',
        'stderr_match': 'depends-on is deprecated',
        'exception_match': None
    },
    {
        'description': 'validate catalog yaml',
        'command_args': [
            'catalog',
            'validate',
            '--as=yaml',
            './oscal-content/nist.gov/SP800-53/rev5/yaml/NIST_SP-800-53_rev5_catalog.yaml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s).',
        'stderr_match': 'depends-on is deprecated',
        'exception_match': None
    },
    {
        'description': 'validate profile json',
        'command_args': [
            'profile',
            'validate',
            '--as=json',
            './oscal-content/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_HIGH-baseline_profile.json'
        ],
        'returncode_match': 0,
        'stdout_match': 'is valid.',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'validate profile xml',
        'command_args': [
            'profile',
            'validate',
            '--as=xml',
            './oscal-content/nist.gov/SP800-53/rev5/xml/NIST_SP-800-53_rev5_HIGH-baseline_profile.xml'
        ],
        'returncode_match': 0,
        'stdout_match': 'is valid.',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'validate profile yaml',
        'command_args': [
            'profile',
            'validate',
            '--as=yaml',
            './oscal-content/nist.gov/SP800-53/rev5/yaml/NIST_SP-800-53_rev5_HIGH-baseline_profile.yaml'
        ],
        'returncode_match': 0,
        'stdout_match': 'is valid.',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'validate assessment-plan json',
        'command_args': [
            'ap',
            'validate',
            '--as=json',
            './fedramp-content/dist/content/templates/sap/json/FedRAMP-SAP-OSCAL-Template.json'
        ],
        'returncode_match': 1,
        'stdout_match': None,
        'stderr_match': "gov.nist.secauto.metaschema.model.common.metapath.function.InvalidTypeFunctionMetapathException: FOTY0012: FOTY0012: Item 'gov.nist.secauto.metaschema.model.common.metapath.item.RequiredValueAssemblyInstanceNodeItemImpl' has no typed value",
        'exception_match': None
    },
    {
        'description': 'validate assessment-plan xml',
        'command_args': [
            'ap',
            'validate',
            '--as=xml',
            './fedramp-content/dist/content/templates/sap/xml/FedRAMP-SAP-OSCAL-Template.xml'
        ],
        'returncode_match': 1,
        'stdout_match': None,
        'stderr_match': "gov.nist.secauto.metaschema.model.common.metapath.function.InvalidTypeFunctionMetapathException: FOTY0012: FOTY0012: Item 'gov.nist.secauto.metaschema.model.common.metapath.item.RequiredValueAssemblyInstanceNodeItemImpl' has no typed value",
        'exception_match': None
    },
    {
        'description': 'validate assessment-plan yaml',
        'command_args': [
            'ap',
            'validate',
            '--as=yaml',
            './fedramp-content/dist/content/templates/sap/yaml/FedRAMP-SAP-OSCAL-Template.yaml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has schema validation issue(s)',
        'stderr_match': '5 schema violations',
        'exception_match': None
    },
    {
        'description': 'validate assessment-results json',
        'command_args': [
            'ar',
            'validate',
            '--as=json',
            './fedramp-content/dist/content/templates/sar/json/FedRAMP-SAR-OSCAL-Template.json'
        ],
        'returncode_match': 1,
        'stdout_match': None,
        'stderr_match': "gov.nist.secauto.metaschema.model.common.metapath.function.InvalidTypeFunctionMetapathException: FOTY0012: FOTY0012: Item 'gov.nist.secauto.metaschema.model.common.metapath.item.RequiredValueAssemblyInstanceNodeItemImpl' has no typed value",
        'exception_match': None
    },
    {
        'description': 'validate assessment-results xml',
        'command_args': [
            'ar',
            'validate',
            '--as=xml',
            './fedramp-content/dist/content/templates/sar/xml/FedRAMP-SAR-OSCAL-Template.xml'
        ],
        'returncode_match': 1,
        'stdout_match': None,
        'stderr_match': "gov.nist.secauto.metaschema.model.common.metapath.function.InvalidTypeFunctionMetapathException: FOTY0012: FOTY0012: Item 'gov.nist.secauto.metaschema.model.common.metapath.item.RequiredValueAssemblyInstanceNodeItemImpl' has no typed value",
        'exception_match': None
    },
    {
        'description': 'validate assessment-results yaml',
        'command_args': [
            'ar',
            'validate',
            '--as=yaml',
            './fedramp-content/dist/content/templates/sar/yaml/FedRAMP-SAR-OSCAL-Template.yaml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has schema validation issue(s)',
        'stderr_match': 'ERROR',
        'exception_match': None
    },
    {
        'description': 'validate poam json',
        'command_args': [
            'poam',
            'validate',
            '--as=json',
            './fedramp-content/dist/content/templates/poam/json/FedRAMP-POAM-OSCAL-Template.json'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s)',
        'stderr_match': 'ERROR',
        'exception_match': None
    },
    {
        'description': 'validate poam xml',
        'command_args': [
            'poam',
            'validate',
            '--as=xml',
            './fedramp-content/dist/content/templates/poam/xml/FedRAMP-POAM-OSCAL-Template.xml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has constraint validation issue(s)',
        'stderr_match': 'ERROR',
        'exception_match': None
    },
    {
        'description': 'validate poam yaml',
        'command_args': [
            'poam',
            'validate',
            '--as=yaml',
            './fedramp-content/dist/content/templates/poam/yaml/FedRAMP-POAM-OSCAL-Template.yaml'
        ],
        'returncode_match': 1,
        'stdout_match': 'has schema validation issue(s)',
        'stderr_match': '2 schema violations found',
        'exception_match': None
    },
    {
        'description': 'metaschema generate-schema xsd',
        'command_args': [
            'metaschema',
            'generate-schema',
            '--as=xml',
            './oscal-content/oscal/src/metaschema/oscal_catalog_metaschema.xml',
            './output/metaschema_generate-schema_xsd/oscal_catalog_metaschema_xsd.xml',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated XML schema file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'metaschema generate-schema json schema',
        'command_args': [
            'metaschema',
            'generate-schema',
            '--as=json',
            './oscal-content/oscal/src/metaschema/oscal_catalog_metaschema.xml',
            './output/metaschema_generate-schema_json/oscal_catalog_metaschema_json-schema.json',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated JSON schema file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'help menu no jansi exception',
        'command_args': [
            'catalog',
            'convert',
            '--help'
        ],
        'returncode_match': 3,
        'stdout_match': 'usage: oscal-cli catalog convert',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert xml json',
        'command_args': [
            'catalog',
            'convert',
            '--to=json',
            './oscal-content/nist.gov/SP800-53/rev5/xml/NIST_SP-800-53_rev5_catalog.xml',
            './output/catalog_convert_xml_json/NIST_SP-800-53_rev5_catalog.json',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated JSON file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert xml yaml',
        'command_args': [
            'catalog',
            'convert',
            '--to=yaml',
            './oscal-content/nist.gov/SP800-53/rev5/xml/NIST_SP-800-53_rev5_catalog.xml',
            './output/catalog_convert_xml_yaml/NIST_SP-800-53_rev5_catalog.yaml',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated YAML file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert json xml',
        'command_args': [
            'catalog',
            'convert',
            '--to=xml',
            './output/catalog_convert_xml_json/NIST_SP-800-53_rev5_catalog.json',
            './output/catalog_convert_json_xml/NIST_SP-800-53_rev5_catalog.xml',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated XML file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert json yaml',
        'command_args': [
            'catalog',
            'convert',
            '--to=yaml',
            './output/catalog_convert_xml_json/NIST_SP-800-53_rev5_catalog.json',
            './output/catalog_convert_json_yaml/NIST_SP-800-53_rev5_catalog.yaml',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated YAML file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert yaml xml',
        'command_args': [
            'catalog',
            'convert',
            '--to=xml',
            './output/catalog_convert_json_yaml/NIST_SP-800-53_rev5_catalog.yaml',
            './output/catalog_convert_yaml_xml/NIST_SP-800-53_rev5_catalog.xml',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated XML file',
        'stderr_match': None,
        'exception_match': None
    },
    {
        'description': 'catalog convert yaml json',
        'command_args': [
            'catalog',
            'convert',
            '--to=json',
            './output/catalog_convert_json_yaml/NIST_SP-800-53_rev5_catalog.yaml',
            './output/catalog_convert_yaml_json/NIST_SP-800-53_rev5_catalog.json',
            '--overwrite'
        ],
        'returncode_match': 0,
        'stdout_match': 'Generated JSON file',
        'stderr_match': None,
        'exception_match': None
    }
]

SCOPED_TESTS = ALL_TESTS
#SCOPED_TESTS = [ALL_TESTS[14]]

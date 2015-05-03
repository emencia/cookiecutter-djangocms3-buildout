"""
Grap all mods doc strings for mods

This script is to be used only to re-generate RST file when you update some mods 
docs.
"""
import imp, os
import StringIO

DESTINATION_PATH = 'project_structure.rst'
TEMPLATE_PATH = '_templates/project_structure.rst'
MODS_DIR_PATH = '../{{cookiecutter.repo_name}}/project/mods_available/'


def import_module_from_path(base_path, module_name):
    """
    Import a module from its base path
    """
    fp, pathname, description = imp.find_module(module_name, [base_path])
    try:
        module = imp.load_module(module_name, fp, pathname, description)
    except:
        return None, None
    finally:
        if fp:
            fp.close()
    return module


def build_doc(document_name, template_path, modsdir_path):
    """
    Grab mods from app template and write a RST document about them
    """
    print "* Writing document '{document}' from path '{path}'".format(document=document_name, path=modsdir_path)
    app_document = StringIO.StringIO()
    
    ## Add RST 'anchor' tag
    #app_document.write(".. _intro_{0}:".format(app))
    #app_document.write('\n')
    
    # Scan available mods
    mods_document = []
    for directory in sorted(os.listdir(modsdir_path)):
        mod_abs = os.path.join(modsdir_path, directory)
        if os.path.isdir(mod_abs):
            # mod title
            print "  - Mod:", directory
            mods_document.append(directory)
            mods_document.append('\n')
            mods_document.append("-"*len(directory))
            mods_document.append('\n\n')
            # mod content
            mod = import_module_from_path(modsdir_path, directory)
            mods_document.append(mod.__doc__.strip())
            mods_document.append('\n\n')
    mods_document = ''.join(mods_document)
    
    # Get the template
    with open(template_path, 'r') as f:
        template = f.read()
        # Get the doc from the base __init__ and replace its 
        # pattern '.. document-mods::' by the mods documentations
        app_document.write(template.strip().replace('.. document-mods::', mods_document))
        app_document.write('\n\n')
    
    # Write the document from template and finded mods docs
    with open(document_name, 'w') as f:
        f.write(app_document.getvalue())
        
    # Clean buffer
    app_document.close()

# Launch document building
build_doc(DESTINATION_PATH, TEMPLATE_PATH, MODS_DIR_PATH)
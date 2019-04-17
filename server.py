from waitress import serve
import library_app.__init__

serve(library_app.__init__.app, host='0.0.0.0', port=80)

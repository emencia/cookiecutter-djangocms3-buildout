# Load the Foundation5 lib
add_import_path "../foundation5/bower_components/foundation/scss"

# Set this to the root of your project when deployed:
http_path = "/static/"
sass_dir = "scss"
css_dir = "../project/webapp_statics/css"
images_dir = "../project/webapp_statics/images"
javascripts_dir = "../project/webapp_statics/js"
fonts_dir = "../project/webapp_statics/fonts"

# You can select your preferred output style here (can be overridden via the command line):
# output_style = :expanded or :nested or :compact or :compressed
output_style = :expanded

# To enable relative paths to assets via compass helper functions. Uncomment:
relative_assets = true

# To disable debugging comments that display the original location of your selectors. Uncomment:
# line_comments = false

# If you prefer the indented syntax, you might want to regenerate this
# project again passing --syntax sass, or you can uncomment this:
# preferred_syntax = :sass
# and then run:
# sass-convert -R --from scss --to sass sass scss && rm -rf sass && mv scss sass

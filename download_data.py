# in the terminal of the wherobots instance, first run:
# aws s3 sync s3://wherobots/usa-structures/ . --profile sc --endpoint-url=https://data.source.coop

# it's good practice to check what is inside the repository that we want to download:
# aws s3 ls s3://wherobots/usa-structures/ --profile sc --endpoint-url=https://data.source.coop

# download everything (note: it could be a large file)
# aws s3 sync s3://wherobots/usa-structures/ . --profile sc --endpoint-url=https://data.source.coop

# optionally, you can download a specific file:
# aws s3 cp s3://wherobots/usa-structures/<PATH_TO_FILE> . --profile sc --endpoint-url=https://data.source.coop

# optionally move the data to a preferred location in your wherobots instance:
# mv usa-structures ~/wherobots_workspace/


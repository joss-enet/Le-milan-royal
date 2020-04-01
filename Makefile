# Linux
COUNT?=50000

#   ______                  __
#  /_  __/__ ________ ____ / /____
#   / / / _ `/ __/ _ `/ -_) __(_-<
#  /_/  \_,_/_/  \_, /\__/\__/___/
#               /___/
default: sql_all

sql_all:
	docker run -it --rm -v $(PWD):/app amancevice/pandas python /app/tools/csv_split.py

sql_partial:
	docker run -it --rm -v $(PWD):/app amancevice/pandas python /app/tools/csv_split_light.py $(COUNT)

#!/usr/bin/env ruby
# matching the sender the reciver and the flag
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")

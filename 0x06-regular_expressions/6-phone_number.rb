#!/usr/bin/env ruby
# mathcing a phone nubmer

puts ARGV[0].scan(/\A[0-9]{10,10}\z/).join

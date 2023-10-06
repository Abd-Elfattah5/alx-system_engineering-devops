#!/usr/bin/env ruby
# matching beginning and ending

puts ARGV[0].scan(/\Ah[a-z]n\z/).join

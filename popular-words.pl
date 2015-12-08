#!/usr/bin/env perl

use strict;
use warnings;
use Cpanel::JSON::XS;

my %words;

while (<STDIN>) {
	my $j = decode_json($_);
	my @words_from_comment = lc($j->{body}) =~ /([a-z']+)/gi;
	$words{$_}++ foreach @words_from_comment;
}

for ( sort { $words{$a} <=> $words{$b} } keys %words) {
	print "$_ - $words{$_}\n";
}

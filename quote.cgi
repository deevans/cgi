#!/usr/bin/perl -tw
# CGI Quote randomizer

print "Content-type: text/html\n\n";

open(QUOTES, "</var/www/html/dee/quotes") || die $!;

my $q = undef;
my @quote = ();
my $i = 1;

for (<QUOTES>) {
	chomp;
	if ($_ eq '%%') {
		if (rand($i) < 1.0) {
			$q = join("\n", @quote);
		}
		$i++;
		@quote = ();
	}
	else {
		push(@quote, $_);
	}
}

close(QUOTES);

print $q;

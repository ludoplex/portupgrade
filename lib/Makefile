
BUILDDIR=	.build

PKGTOOLS_SRC=	pkg.py \
		pkgdb.py \
		pkgdbtools.py \
		pkginfo.py \
		pkgmisc.py \
		pkgtools.py \
		pkgtsort.py \
		pkgversion.py \
		portinfo.py \
		ports.py \
		portsdb.py

FILESGROUPS=	FILES PKGTOOLSFILES
FILES=		pkgtools.rb
PKGTOOLSFILES=	${PKGTOOLS_SRC:S,^,${BUILDDIR}/,g} pkgtools/revision.rb

.include "${.CURDIR}/Makefile.inc"

FILESDIR?=	${RUBY_SITELIBDIR}
PKGTOOLSFILESDIR=	${FILESDIR}/pkgtools

CLEANDIRS=	${BUILDDIR}

.for file in ${PKGTOOLS_SRC}
${BUILDDIR}/${file}: pkgtools/${file}
	${PYTHON} -m py_compile ${.ALLSRC}
	@${MKDIR} ${BUILDDIR}/
	${PYTHON} -c \
		"import fileinput, sys; [sys.stdout.write(line.replace('/usr/local', '${PREFIX}')) for line in fileinput.input()]"
		${.ALLSRC} > ${.TARGET}
.endfor

pkgtools/revision.rb: pkgtools/revision.rb.in ${.CURDIR}/../scripts/buildrev.sh .PHONY
	${.CURDIR}/../scripts/buildrev.sh

beforeinstall: install-mkdir

install-mkdir: .PHONY
	${MKDIR} ${DESTDIR}${PKGTOOLSFILESDIR}

.include <bsd.prog.mk>

.include "${.CURDIR}/../Makefile.compat"

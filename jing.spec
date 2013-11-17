Summary:	Application for validating XML document against a RELAX NG schema
Summary(pl.UTF-8):	Aplikacja do sprawdzania poprawności dokumentu XML względem schematu RELAX NG
Name:		jing
Version:	20091111
Release:	1
License:	BSD
Group:		Applications/Text
#Source0Download: http://code.google.com/p/jing-trang/downloads/list
Source0:	http://jing-trang.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	13eef193921409a1636377d1efbf9843
URL:		http://code.google.com/p/jing-trang/
Requires:	java-isorelax >= 20041111
Requires:	java-xerces >= 2.9.1
Requires:	jre
Requires:	saxon >= 6.5.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jing is an application for validating an XML document against a RELAX
NG schema, in either the XML or the compact syntax.

%description -l pl.UTF-8
Jing to aplikacja do sprawdzania poprawności dokumentu XML względem
schematu RELAX NG, zarówno w formacie XML, jak i zwięzłym.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir},%{_datadir}/jing}

cp -a lib/* $RPM_BUILD_ROOT%{_datadir}/jing
install bin/jing.jar $RPM_BUILD_ROOT%{_javadir}

cat >$RPM_BUILD_ROOT%{_bindir}/jing <<'EOF'
#!/bin/sh

java -jar %{_javadir}/jing.jar "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.html doc
%attr(755,root,root) %{_bindir}/jing
%{_javadir}/jing.jar
%{_datadir}/jing

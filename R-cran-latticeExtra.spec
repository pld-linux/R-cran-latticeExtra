%define		fversion	%(echo %{version} |tr r -)
%define		modulename	latticeExtra
Summary:	Extra Graphical Utilities Based on Lattice
Name:		R-cran-%{modulename}
Version:	0.6r26
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	f17954ceb5333c1a9bd7fe3f175aac6c
URL:		http://latticeextra.r-forge.r-project.org/
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extra graphical utilities based on lattice.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

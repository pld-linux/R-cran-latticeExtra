%define		fversion	%(echo %{version} |tr r -)
%define		modulename	latticeExtra
%undefine	_debugsource_packages
Summary:	Extra Graphical Utilities Based on Lattice
Name:		R-cran-%{modulename}
Version:	0.6r31
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	355ce56f2895fd791612a698f0404000
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

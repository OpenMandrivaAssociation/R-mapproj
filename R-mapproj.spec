%global packname  mapproj
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.1
Release:          2
Summary:          Map Projections
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/mapproj_1.2-1.tar.gz
Requires:         R-maps 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-maps

%description
Converts latitude/longitude into projected coordinates.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1_8.3-1
+ Revision: 776340
- Import R-mapproj
- Import R-mapproj




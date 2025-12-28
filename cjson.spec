Summary:	Ultralightweight JSON parser in ANSI C
Summary(pl.UTF-8):	Ultralekki parser formatu JSON napisany w ANSI C
Name:		cjson
Version:	1.7.19
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/DaveGamble/cJSON/releases
Source0:	https://github.com/DaveGamble/cJSON/archive/v%{version}/cJSON-%{version}.tar.gz
# Source0-md5:	60d39f4f639a90907b305b36727430e1
URL:		https://github.com/DaveGamble/cJSON
BuildRequires:	cmake >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cJSON aims to be the dumbest possible parser that you can get your job
done with. It's a single file of C, and a single header file.

%description -l pl.UTF-8
cJSON jest tworzony jako możliwie najprostszy parser wykonujący swoje
zadanie. Jest to pojedynczy plik w C i pojedynczy plik nagłówkowy.

%package devel
Summary:	Header files for cJSON library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cJSON
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cJSON library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cJSON.

%prep
%setup -q -n cJSON-%{version}

%build
install -d build
cd build
%cmake .. \
	-DENABLE_CJSON_TEST:BOOL=OFF \
	-DENABLE_CJSON_UTILS:BOOL=ON

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md SECURITY.md
%{_libdir}/libcjson.so.*.*.*
%ghost %{_libdir}/libcjson.so.1
%{_libdir}/libcjson_utils.so.*.*.*
%ghost %{_libdir}/libcjson_utils.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcjson.so
%{_libdir}/libcjson_utils.so
%{_includedir}/cjson
%{_pkgconfigdir}/libcjson.pc
%{_pkgconfigdir}/libcjson_utils.pc
%{_libdir}/cmake/cJSON

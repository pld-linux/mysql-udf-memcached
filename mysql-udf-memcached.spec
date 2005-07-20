# TODO
# - correct package naming if there's better naming schema (mysql-udf-memcached?)?
# - i've installed .so to %{_libdir} because straced mysqld searched
#   same path as dlopen() would do (/lib:/lib/tls:/usr/lib). perhaps
#   %{_libdir}/mysql would be more appropriate (but then need to
#   insert .so with full path? patch mysqld?)
Summary:	Memcached UDF for MySQL
Summary(pl):	Memcached UDF dla MySQLa
Name:		mysql-udf-memcached
Version:	0
Release:	0.2
Epoch:		0
# probably BSD will ask jan
License:	BSD
Group:		Applications/Databases
Source0:	http://jan.kneschke.de/projects/mysql/udf/udf_memcache.c
# Source0-md5:	0457d875b25ba74621c50b949f22a8f6
Source1:	http://jan.kneschke.de/projects/mysql/udf/create-function-memcache.sql
# Source1-md5:	c80b1ec746c72f2a09e7204bfaaf2409
URL:		http://jan.kneschke.de/projects/mysql/udf/
BuildRequires:	libmemcache-devel >= 1.3.0
BuildRequires:	mysql-devel
Requires:	mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL UDF interface to memcached.

%description -l pl
MySQLowy interfejs UDF do memcached.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
%{__cc} %{rpmcflags} -DDBUG_OFF -shared -o udf_memcache.so udf_memcache.c \
	-lmemcache $(mysql_config --cflags)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install udf_memcache.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc create-function-memcache.sql
%attr(755,root,root) %{_libdir}/*.so

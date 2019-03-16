#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-varImp
Version  : 0.2
Release  : 4
URL      : https://cran.r-project.org/src/contrib/varImp_0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/varImp_0.2.tar.gz
Summary  : RF Variable Importance for Arbitrary Measures
Group    : Development/Tools
License  : GPL-3.0
Requires: R-TH.data
Requires: R-measures
Requires: R-party
BuildRequires : R-TH.data
BuildRequires : R-measures
BuildRequires : R-party
BuildRequires : buildreq-R

%description
# varImp
Random forest variable importance for arbitrary measures of the [measures](https://github.com/mlr-org/measures) package, which contains the biggest collection of measures for regression and classification in R.

%prep
%setup -q -c -n varImp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533752080

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1533752080
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library varImp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library varImp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library varImp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library varImp|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/varImp/DESCRIPTION
/usr/lib64/R/library/varImp/INDEX
/usr/lib64/R/library/varImp/Meta/Rd.rds
/usr/lib64/R/library/varImp/Meta/features.rds
/usr/lib64/R/library/varImp/Meta/hsearch.rds
/usr/lib64/R/library/varImp/Meta/links.rds
/usr/lib64/R/library/varImp/Meta/nsInfo.rds
/usr/lib64/R/library/varImp/Meta/package.rds
/usr/lib64/R/library/varImp/NAMESPACE
/usr/lib64/R/library/varImp/R/varImp
/usr/lib64/R/library/varImp/R/varImp.rdb
/usr/lib64/R/library/varImp/R/varImp.rdx
/usr/lib64/R/library/varImp/help/AnIndex
/usr/lib64/R/library/varImp/help/aliases.rds
/usr/lib64/R/library/varImp/help/paths.rds
/usr/lib64/R/library/varImp/help/varImp.rdb
/usr/lib64/R/library/varImp/help/varImp.rdx
/usr/lib64/R/library/varImp/html/00Index.html
/usr/lib64/R/library/varImp/html/R.css

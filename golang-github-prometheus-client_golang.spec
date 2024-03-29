# https://github.com/prometheus/client_golang
%global goipath github.com/prometheus/client_golang
%global commit  180b8fdc22b4ea7750bcb43c925277654a1ea2f3

%gometa

Name:           golang-github-prometheus-client_golang
Version:        0.9.0
Release:        0.3%{?dist}
Summary:        Prometheus instrumentation library for Go applications
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

# Patch to disable tests which require network connection
Patch0:         00-disable-networking-tests.patch

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/beorn7/perks/quantile)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/prometheus/procfs)
BuildRequires:  golang(golang.org/x/net/context)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q
%patch0 -p1


%install
%goinstall glide.lock glide.yaml


%check
%gochecks -d prometheus


%files devel -f devel.file-list
%license LICENSE
%doc README.md MAINTAINERS.md CONTRIBUTING.md CHANGELOG.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.3.git180b8fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.9.0-0.2.git180b8fd
- Upload glide files

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-0.1.20180526git180b8fd
- Update to 0.9.0 pre snapshot to fix syncthing builds.
- Update to spec 3.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.0-7
- Bump to upstream c5b7fccd204277076155f10851dad72b76a49317
  related: #1214784

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0.7.0-4
- Bump to upstream 449ccefff16c8e2b7229f6be1921ba22f62461fe
  related: #1214784

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 jchaloup <jchaloup@redhat.com> - 0.7.0-1
- Bump to upstream e51041b3fa41cece0dca035740ba6411905be473
  related: #1214784

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0.6.0-3
- Add Godeps.json to doc
  related: #1214784

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.6.0-2
- Update spec file to spec-2.0
- Disabled failing test prometheus
- Disabled failing test model
  resolves: #1214784

* Thu Jul 23 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.6.0-1
- Bump to upstream 36659fa1ad85ee0dd33822b68a192a814c93a57b
  related: #1214784

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-1
- Bump to upstream b0bd7e1be33327b85cb4853e7011156e3cedd657
  related: #1214784

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0.4.0-1
- Bump to upstream 608ec8b69e284600a7ad1b36514a1e6876e22b9f
  resolves: #1214784

* Wed Mar 04 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gite5098ac
- Bump to upstream e5098ac1ff13c7f85b68b120b253dd834ba49682
  related: #1190442

* Thu Feb 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git39e4bc8
- Bump to upstream 39e4bc83f974fb141a9e67c042b26322bacc917b
  related: #1190442

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git52186fc
- First package for Fedora
  resolves: #1190442


// src/pages/Home.js
export default function Home() {
    return (
        <div className="container mt-5 text-center">
            <h1 className="display-4 fw-bold mb-3">Hestia</h1>
            <p className="lead mb-4">Your threat intelligence/ASPM platform</p>
            <button className="btn btn-primary btn-lg px-4">Try the demo</button>

            {/* Cards de funciones */}
            <div className="row mt-5">
                <div className="col-md-4">
                    <div className="card h-100 border-0">
                        <div className="card-body">
                            <h5>Threat Detection</h5>
                            <p>AI-driven analysis of network traffic and logs.</p>
                        </div>
                    </div>
                </div>
                <div className="col-md-4">
                    <div className="card h-100 border-0">
                        <div className="card-body">
                            <h5>Incident Response</h5>
                            <p>Automated playbooks and real-time alerts.</p>
                        </div>
                    </div>
                </div>
                <div className="col-md-4">
                    <div className="card h-100 border-0">
                        <div className="card-body">
                            <h5>Reporting & Analytics</h5>
                            <p>Custom dashboards and compliance reports.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
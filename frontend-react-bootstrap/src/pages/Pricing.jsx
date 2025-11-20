// src/pages/Pricing.js


export default function Pricing() {
    return (
        <div className="container my-5">
            <h2 className="text-center mb-5">PRICING</h2>
            <div className="row g-4 justify-content-center">
                {/* Standard */}
                <div className="col-md-4">
                    <div className="card border-primary h-100" >
                        <div className="card-body text-center p-4">
                            <h5>Standard</h5>
                            <h2 className="mb-3">$500<span className="text-muted fw-normal">/month</span></h2>
                            <ul className="list-unstyled mt-3 text-start">
                                <li><i className="bi bi-check-circle-fill me-2 text-primary"></i>Continuous code scanning (code, dependencies, containers)</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-primary"></i>Access to unified dashboard</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-primary"></i>Mark false positives and filter by severity</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-primary"></i>PDF/JSON export of reports</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-primary"></i>Ideal for small teams or individual developers</li>
                            </ul>
                            <button className="btn btn-outline-primary w-100 mt-3">TRY NOW</button>
                        </div>
                    </div>
                </div>

                {/* Premium */}
                <div className="col-md-4">
                    <div className="card border-warning h-100" >
                        <div className="card-body text-center p-4">
                            <h5>Premium</h5>
                            <h2 className="mb-3">$2000<span className="text-muted fw-normal">/month</span></h2>
                            <ul className="list-unstyled mt-3 text-start">
                                <li><i className="bi bi-check-circle-fill me-2 text-warning"></i>All Standard features</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-warning"></i>CI/CD Integration (GitHub, GitLab, Jenkins)</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-warning"></i>Advanced prioritization and trend tracking</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-warning"></i>Priority support</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-warning"></i>Best for growing teams and mid-size companies</li>
                            </ul>
                            <button className="btn btn-warning text-white w-100 mt-3">TRY NOW</button>
                        </div>
                    </div>
                </div>

                {/* Enterprise */}
                <div className="col-md-4">
                    <div className="card border-dark h-100" >
                        <div className="card-body text-center p-4">
                            <h5>Enterprise</h5>
                            <h2 className="mb-3">Custom</h2>
                            <ul className="list-unstyled mt-3 text-start">
                                <li><i className="bi bi-check-circle-fill me-2 text-dark"></i>All Premium features</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-dark"></i>Dedicated account manager and onboarding</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-dark"></i>Custom roles and policies</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-dark"></i>Enterprise-level security and compliance</li>
                                <li><i className="bi bi-check-circle-fill me-2 text-dark"></i>Perfect for large organizations with complex workflows</li>
                            </ul>
                            <button className="btn btn-outline-dark w-100 mt-3">CONTACT US</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
// src/pages/Blog.js
export default function Blog() {
    return (
        <div className="container my-5">
            <h2 className="mb-4">Latest from the Blog</h2>
            <div className="row">
                <div className="col-md-6 mb-4">
                    <div className="card">
                        <img src="https://via.placeholder.com/300x150" alt="Blog post" className="card-img-top" />
                        <div className="card-body">
                            <h5>New AI Model Improves Threat Accuracy by 40%</h5>
                            <small className="text-muted">October 15, 2025</small>
                            <p className="mt-2">Our latest neural network reduces false positives...</p>
                            <a href="continue-ai-model" className="btn btn-outline-primary btn-sm">Continue reading</a>
                        </div>
                    </div>
                </div>
                <div className="col-md-6 mb-4">
                    <div className="card">
                        <img src="https://via.placeholder.com/300x150" alt="Blog post" className="card-img-top" />
                        <div className="card-body">
                            <h5>Best Practices for SOC Teams in 2025</h5>
                            <small className="text-muted">October 10, 2025</small>
                            <p className="mt-2">How to optimize your security operations center...</p>
                            <a href="continue-best-practice" className="btn btn-outline-primary btn-sm">Continue reading</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
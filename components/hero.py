import streamlit.components.v1 as components
from utils import config as cfg


def render(st):
    """Hero section with a real WebGL 3D scene (Three.js via CDN, embedded
    as an HTML component). The scene, headline, and CTAs all live inside
    the same iframe document so the text can sit over the 3D canvas.
    CTAs use target="_top" so clicking them scrolls the actual Streamlit
    page (outside the iframe), not the iframe itself."""

    html = f"""
    <div id="hero-root" style="position:relative; width:100%; height:560px; overflow:hidden; border-radius:16px;
         border:1px solid #26314E; background:#0B1120;">
      <canvas id="hero-canvas" style="position:absolute; inset:0; width:100%; height:100%; display:block;"></canvas>

      <div style="position:relative; z-index:2; height:100%; display:flex; flex-direction:column;
                  justify-content:center; padding: 0 3rem; max-width: 720px;
                  font-family:'Manrope', -apple-system, sans-serif;">
        <div style="display:inline-flex; align-items:center; gap:0.5rem; color:#5FA8D3;
                    font-weight:700; font-size:0.95rem; margin-bottom:1rem;">
          <span style="width:7px;height:7px;border-radius:50%;background:#6FCF97;
                       box-shadow:0 0 0 4px rgba(111,207,151,0.15);"></span>
          Open to internships
        </div>
        <h1 style="font-family:'Newsreader', Georgia, serif; font-weight:500; letter-spacing:-0.01em;
                   color:#E8ECF4; font-size:clamp(2rem, 4.2vw, 3.1rem); line-height:1.12;
                   margin:0 0 1.1rem 0;">{cfg.HEADLINE}</h1>
        <p style="color:#8B96AC; font-size:1.05rem; max-width:52ch; margin:0 0 2rem 0;">
          {cfg.SUBHEADLINE}
        </p>
        <div style="display:flex; gap:0.9rem; flex-wrap:wrap;">
          <a href="#{cfg.PRIMARY_CTA_TARGET}" target="_top"
             style="display:inline-block; padding:0.7rem 1.4rem; border-radius:8px; font-weight:700;
                    font-size:0.95rem; text-decoration:none; background:#E8A33D; color:#1A1200;">
            {cfg.PRIMARY_CTA_LABEL}
          </a>
          <a href="#{cfg.SECONDARY_CTA_TARGET}" target="_top"
             style="display:inline-block; padding:0.7rem 1.4rem; border-radius:8px; font-weight:700;
                    font-size:0.95rem; text-decoration:none; background:transparent; color:#E8ECF4;
                    border:1px solid #26314E;">
            {cfg.SECONDARY_CTA_LABEL}
          </a>
        </div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
    (function() {{
        var root = document.getElementById('hero-root');
        var canvas = document.getElementById('hero-canvas');
        var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        var width = root.clientWidth;
        var height = root.clientHeight;

        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(55, width / height, 0.1, 1000);
        camera.position.z = 34;

        var renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setSize(width, height);

        // --- Build a "data network": points + connecting lines ---
        var NODE_COUNT = 70;
        var RADIUS = 16;
        var positions = [];
        var nodeGeo = new THREE.SphereGeometry(0.16, 8, 8);
        var nodeMat = new THREE.MeshBasicMaterial({{ color: 0xE8A33D }});
        var nodesGroup = new THREE.Group();
        var nodeMeshes = [];

        for (var i = 0; i < NODE_COUNT; i++) {{
            var theta = Math.random() * Math.PI * 2;
            var phi = Math.acos((Math.random() * 2) - 1);
            var r = RADIUS * (0.55 + Math.random() * 0.45);
            var x = r * Math.sin(phi) * Math.cos(theta);
            var y = r * Math.sin(phi) * Math.sin(theta);
            var z = r * Math.cos(phi);
            positions.push(new THREE.Vector3(x, y, z));

            var mesh = new THREE.Mesh(nodeGeo, nodeMat);
            mesh.position.set(x, y, z);
            nodesGroup.add(mesh);
            nodeMeshes.push(mesh);
        }}

        // Connect nearby nodes with thin lines
        var lineMat = new THREE.LineBasicMaterial({{ color: 0x5FA8D3, transparent: true, opacity: 0.25 }});
        var linePositions = [];
        var MAX_DIST = 8.5;
        for (var a = 0; a < positions.length; a++) {{
            for (var b = a + 1; b < positions.length; b++) {{
                if (positions[a].distanceTo(positions[b]) < MAX_DIST) {{
                    linePositions.push(positions[a].x, positions[a].y, positions[a].z);
                    linePositions.push(positions[b].x, positions[b].y, positions[b].z);
                }}
            }}
        }}
        var lineGeo = new THREE.BufferGeometry();
        lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
        var lines = new THREE.LineSegments(lineGeo, lineMat);

        scene.add(nodesGroup);
        scene.add(lines);

        var mouseX = 0, mouseY = 0;
        root.addEventListener('mousemove', function(e) {{
            var rect = root.getBoundingClientRect();
            mouseX = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
            mouseY = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
        }});

        var clock = new THREE.Clock();
        var running = true;

        function animate() {{
            if (!running) return;
            requestAnimationFrame(animate);
            if (document.hidden) return;

            var t = clock.getElapsedTime();
            var autoRotate = reduceMotion ? 0.02 : 0.06;

            nodesGroup.rotation.y = t * autoRotate + mouseX * 0.3;
            nodesGroup.rotation.x = mouseY * 0.2;
            lines.rotation.y = nodesGroup.rotation.y;
            lines.rotation.x = nodesGroup.rotation.x;

            renderer.render(scene, camera);
        }}
        animate();

        window.addEventListener('resize', function() {{
            width = root.clientWidth;
            height = root.clientHeight;
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
        }});
    }})();
    </script>
    """

    components.html(html, height=580, scrolling=False)

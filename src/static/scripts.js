// Script para Upload de Arquivos
const uploadForm = document.getElementById('upload-form');
if (uploadForm) {
    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fileInput = document.getElementById('file-input');
        const tableName = document.getElementById('table-name').value;
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('file', file);
        formData.append('name', tableName);

        try {
            const response = await fetch('/upload_file', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            document.getElementById('result').innerHTML = `
                <div class="message success">
                    <i class="fas fa-check-circle"></i> Tabela ${tableName} enviada com sucesso!
                </div>`;
        } catch (error) {
            document.getElementById('result').innerHTML = `
                <div class="message error">
                    <i class="fas fa-times-circle"></i> Ocorreu um erro ao enviar o arquivo.
                </div>`;
        }
    });
}

// Script para Carregar Dados
const loadDataButton = document.getElementById('load-data');
if (loadDataButton) {
    loadDataButton.addEventListener('click', async () => {
        const tableDiv = document.getElementById('data-table');
        const tableName = document.getElementById('table-name');
        tableDiv.innerHTML = '<div class="loading"><i class="fas fa-spinner fa-spin"></i> Carregando dados...</div>';

        try {
            const response = await fetch(`/api/v1/query?q=SELECT * FROM ${tableName} LIMIT 100`);
            const data = await response.json();

            if (data.result && data.result.length > 0) {
                let table = '<table><thead><tr>';
                // Cabeçalhos
                for (let key in data.result[0]) {
                    table += `<th>${key}</th>`;
                }
                table += '</tr></thead><tbody>';
                // Dados
                data.result.forEach(row => {
                    table += '<tr>';
                    for (let key in row) {
                        table += `<td>${row[key]}</td>`;
                    }
                    table += '</tr>';
                });
                table += '</tbody></table>';
                tableDiv.innerHTML = table;
            } else {
                tableDiv.innerHTML = `
                    <div class="message info">
                        <i class="fas fa-info-circle"></i> Nenhum dado encontrado.
                    </div>`;
            }
        } catch (error) {
            tableDiv.innerHTML = `
                <div class="message error">
                    <i class="fas fa-times-circle"></i> Ocorreu um erro ao carregar os dados.
                </div>`;
        }
    });
}

// Script para Executar Consultas
const queryForm = document.getElementById('query-form');
if (queryForm) {
    queryForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const queryInput = document.getElementById('query');
        const query = queryInput.value.trim();
        const resultDiv = document.getElementById('query-result');
        resultDiv.innerHTML = '<div class="loading"><i class="fas fa-spinner fa-spin"></i> Executando consulta...</div>';

        try {
            const response = await fetch('/api/v1/query?q=' + encodeURIComponent(query));

            const data = await response.json();

            if (data.result && data.result.length > 0) {
                let table = '<table><thead><tr>';
                // Cabeçalhos
                for (let key in data.result[0]) {
                    table += `<th>${key}</th>`;
                }
                table += '</tr></thead><tbody>';
                // Dados
                data.result.forEach(row => {
                    table += '<tr>';
                    for (let key in row) {
                        table += `<td>${row[key]}</td>`;
                    }
                    table += '</tr>';
                });
                table += '</tbody></table>';
                resultDiv.innerHTML = table;
            } else {
                resultDiv.innerHTML = `
                    <div class="message info">
                        <i class="fas fa-info-circle"></i> Nenhum dado encontrado.
                    </div>`;
            }
        } catch (error) {
            resultDiv.innerHTML = `
                <div class="message error">
                    <i class="fas fa-times-circle"></i> Ocorreu um erro ao executar a consulta.
                </div>`;
        }
    });
}


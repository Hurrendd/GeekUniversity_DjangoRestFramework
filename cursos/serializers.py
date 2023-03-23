from django.db.models import Avg
from rest_framework import serializers

from cursos.models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError(
            'The field "Avaliacao" needs to be a number between 1 and 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested RelationShip
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='avaliacao-detail')

    media_avaliacoes = serializers.SerializerMethodField()

    # PrimaryKey Related Ship
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media * 2) / 2

    def validate_titulo(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                'Titulo nao pode ter menos que 10 caracteres.')
        return value
